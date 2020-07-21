# pmapv

> A parallel map into vector

Pretty much a combination of clojure's [pmap](https://clojuredocs.org/clojure.core/pmap) and [mapv](https://clojuredocs.org/clojure.core/mapv)
 
Usage: [pip](https://pypi.org/project/pmapv/)

```python
from pmapv import pflatmapv, pmapv

add1 = lambda x: x + 1

pflatmapv(add1, [[1], [2], [3]])
# => [2, 3, 4]

pmapv(add1, [1, 2, 3])
# => [2, 3, 4]
```
