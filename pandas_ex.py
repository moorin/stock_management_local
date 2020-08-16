import pandas as pd                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          import pandas as pd
import numpy as np

data = {'name':['moo','hye','han'],'year':[2010,2011,2012]}
# column의 이름, 값들

df = pd.DataFrame(data)
# index(row)의 이름을 지정해주지 않으면 0,1,2가 디폴트

df2 = pd.DataFrame(data, columns = ['year','name','penalty'], index = ['one','two','three'])

# column이름, 값들 추가
df2['penalty'] = [0.1, 0.2, 0.3]
df2['zeros'] = np.arange(3)
# 모든 값을 0.5로 바꾸기
#df['penalty'] = 0.5


#DataFrame Indexing
#df = pd.DataFrame(data, columns=["year", "names", "points", "penalty"], index=["one", "two", "three", "four", "five"])

#column을 선택해서 값 출력하기
print(df['year'])
# df.year 이것과 똑같다.
# df[['year'],'points']

#데이터 가공
#df['high_points'] = df['net_points'] > 2.0

# col 삭제하기
#del df['high_points']

# col two ~ four까지 출력
df.loc['two':'four']
#df.loc['two':'four', 'points']
# 3번째 row을 가져온다.
# df.iloc[3]

# col, row
# df.iloc[3:5, 0:2]
# 어떤 특정 값 df.iloc[1,1]

# 새로운 행 삽입하기
#df.loc['six',:] = [2013,'Jun',4.0,0.1,2.1]

#출처: https://doorbw.tistory.com/172 [Tigercow.Door]

#df.loc[(df['points']>2)&(df['points']<3),:]

# 새로운 값을 대입할 수도 있다.
# df.loc[df['points'] > 3, 'penalty'] = 0


print(df)
print(df2)

