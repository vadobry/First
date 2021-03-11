import matplotlib.pyplot as pyplot

labels = ("Home", "Work", "Shopping")
sizes = [38.4, 61.3, 10.3]
patches, texts = pyplot.pie(sizes)
pyplot.legend(patches, labels)
pyplot.axis("equal")
pyplot.tight_layout()
pyplot.show()
