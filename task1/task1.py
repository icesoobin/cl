import dpkt
import matplotlib.pyplot as plt

loadingTime = []
for idx in range(1, 100):
  start = None
  end = None
  for ts, pkt in dpkt.pcap.Reader(open("http2/{:03d}.pcap".format(idx),'rb')):
    if not start:
      start = ts
    end = ts
  loadingTime.append(end - start)
plt.boxplot(loadingTime)
plt.show()
