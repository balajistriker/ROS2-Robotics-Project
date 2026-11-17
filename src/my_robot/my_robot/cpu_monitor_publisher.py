import rclpy
from rclpy.node import Node 
from std_msgs.msg import String 
import psutil
import json
import subprocess
from datetime import datetime
class CPUMonitor(Node):
    def __init__(self):
         super().__init__('cpu_monitor')
         self.publisher =self.create_publisher(String, '/cpu_monitor',10)
         self.timer = self.create_timer(1.0, self.publish_cpu_usage)
         # Initialize CPU measurements
         psutil.cpu_percent(interval=None)

         for process in psutil.process_iter():
                try:
                    process.cpu_percent(interval=None)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

         self.get_logger().info(
                'CPU and GPU Monitor Publisher Started'
            )
            # Collect CPU Applications
    def get_cpu_applications(self):

        applications = []

        for process in psutil.process_iter(
            ['pid', 'name']
        ):

            try:

                cpu_usage = process.cpu_percent(
                    interval=None
                )

                if cpu_usage > 0:

                    applications.append({
                        'name': process.info['name'],
                        'pid': process.info['pid'],
                        'cpu_percent': cpu_usage
                    })

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied
            ):
                continue

        applications.sort(
            key=lambda x: x['cpu_percent'],
            reverse=True
        )

        return applications[:10]

    # Collect GPU Applications
    def get_gpu_applications(self):

        applications = []

        try:

            result = subprocess.run(
                [
                    'nvidia-smi',
                    '--query-compute-apps=pid,process_name,used_gpu_memory',
                    '--format=csv,noheader,nounits'
                ],
                capture_output=True,
                text=True,
                timeout=3
            )

            if result.returncode != 0:
                return applications

            for line in result.stdout.strip().splitlines():

                if not line.strip():
                    continue

                values = line.split(',', 2)

                if len(values) != 3:
                    continue

                applications.append({
                    'pid': int(values[0].strip()),
                    'name': values[1].strip(),
                    'gpu_memory_mb': int(
                        values[2].strip().split()[0]
                    )
                })

        except (
            FileNotFoundError,
            subprocess.TimeoutExpired,
            ValueError
        ):
            pass

        return applications

    # Collect Overall GPU Usage
    def get_gpu_usage(self):

        try:

            result = subprocess.run(
                [
                    'nvidia-smi',
                    '--query-gpu=utilization.gpu,memory.used,memory.total',
                    '--format=csv,noheader,nounits'
                ],
                capture_output=True,
                text=True,
                timeout=3
            )

            if result.returncode != 0:
                return None

            values = result.stdout.strip().split(',')

            return {
                'usage_percent': float(values[0].strip()),
                'memory_used_mb': int(values[1].strip()),
                'memory_total_mb': int(values[2].strip())
            }

        except (
            FileNotFoundError,
            subprocess.TimeoutExpired,
            ValueError,
            IndexError
        ):
            return None
      # Publish System Data
    def publish_cpu_usage(self):

        system_data = {

            'timestamp': datetime.now().isoformat(),

            'cpu': {
                'usage_percent': psutil.cpu_percent(
                    interval=None
                ),

                'applications': self.get_cpu_applications()
            },

            'gpu': {
                'usage_percent': psutil.gpu_percent(interval=None) if hasattr(psutil, 'gpu_percent') else None,

                'applications': self.get_gpu_applications()
            }
        }

        # Convert Dictionary to JSON
        msg = String()

        msg.data = json.dumps(system_data)

        # Publish
        self.publisher.publish(msg)

        self.get_logger().info(
            f"CPU_Usage...: "
            f"{system_data['cpu']['usage_percent']}%"
        )  
        self.get_logger().info(f"GPU_Usage...: {system_data['gpu']['usage_percent']}%")
def main(args=None):
    rclpy.init(args=args)
    node = CPUMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()             