class LeakyBucket():
  def __init__(self, bucket_size, output_rate, input_packets):
    self.bucket_size = bucket_size
    self.output_rate = output_rate
    self.input_packets = input_packets

  def run(self):
    for i in range(len(self.input_packets)):
      packet_size = self.input_packets[i]
      print(f"Packet No: {i} Packet Size: {packet_size}")

      if packet_size > self.bucket_size:
        print("\t Bucket Overflow!!!")
      else:
        while packet_size > self.output_rate:
          print(f"\t {self.output_rate} bytes sent")
          packet_size -= self.output_rate

        if packet_size:
          print(f"\t Last {packet_size} bytes sent")
        
        print("\t Bucket output successful \n")


bucket_size = int(input("Enter Bucket Size: "))
output_rate = int(input("Enter Output Rate: "))
input_packets = list(map(int, input("Enter Input Packets: ").split()))

leaky_bucket = LeakyBucket(bucket_size, output_rate, input_packets)
leaky_bucket.run()
