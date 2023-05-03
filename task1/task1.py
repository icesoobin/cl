import dpkt
import matplotlib.pyplot as plt

http2LoadingTime = []
for idx in range(1, 100):
  start = None
  end = None
  for ts, pkt in dpkt.pcap.Reader(open("http2/{:03d}.pcap".format(idx),'rb')):
    if not start:
      start = ts
    end = ts
  http2LoadingTime.append(end - start)
bp1 = plt.boxplot(http2LoadingTime)

quic2LoadingTime = []
for idx in range(1, 100):
  start = None
  end = None
  for ts, pkt in dpkt.pcap.Reader(open("quic/{:03d}.pcap".format(idx),'rb')):
    if not start:
      start = ts
    end = ts
  quic2LoadingTime.append(end - start)
bp2 = plt.boxplot(quic2LoadingTime)

plt.legend([bp1["boxes"][0], bp2["boxes"][0]], ['HTTP/2', 'QUIC'], loc='upper right')
plt.show()
plt.savefig('task1.png')
