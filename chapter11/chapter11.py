# CHAPTER 11 모듈과 패키지

# 11.2.1 모듈 탐색 경로
import sys
for place in sys.path:
    print(place)

import sys
sys.path.insert(0, "/my/modules")

# 11.2.2 상대/절대 경로 임포트

# 11.2.3 네임스페이스 패키지
from critters import wendigo, rougarou

# 11.2.4 모듈 vs 객체

