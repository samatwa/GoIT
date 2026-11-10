# goit-algo-hw-05

## Task 3: substring-search benchmark

The original Ukrainian search strings are described here as a present substring ("search") and an absent substring ("delegation"). The benchmark inputs remain unchanged in the source files.

| Article | Substring | Boyer–Moore time | KMP time | Rabin–Karp time |
|---|---|---:|---:|---:|
| article1.txt | Present | 0.02696789999026805 | 0.043457900057546794 | 0.11293509998358786 |
| article1.txt | Absent | 0.7001314000226557 | 2.038023400004022 | 5.04281309992075 |
| article2.txt | Present | 0.09996489994227886 | 0.2459911999758333 | 0.578131000045687 |
| article2.txt | Absent | 1.0447633999865502 | 3.0047439999179915 | 7.44463739998173 |

Boyer–Moore was fastest in these tests, followed by KMP and Rabin–Karp. Each algorithm took longer for the absent substring. These recorded measurements describe the tested articles and inputs rather than a universal ranking.
