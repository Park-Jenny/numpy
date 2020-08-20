#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[8]:


arr=np.array([0,1,2,3,4,5,6,7,8,9])


# In[9]:


arr


# In[10]:


type(arr)


# In[11]:


#array의 형태를 확인


# In[12]:


arr.shape


# In[13]:


#말을 왜 이렇게 느리게 하세요;;; 진짜 답답해 죽겠네


# In[14]:


#array의 자료형을 확인


# In[15]:


arr.dtype


# In[17]:


data=[0,1,2,3,4,5,6,7,8,9]
x=np.array(data)
x


# In[18]:


2*x


# In[20]:


a=np.array([1,2,3])
b=np.array([10,20,30])


# In[21]:


2*a+b


# In[22]:


2*(a+b)


# In[23]:


b-a


# In[24]:


b/a


# In[25]:


a==2


# In[26]:


b>10


# In[27]:


(a==2)&(b>10) # &라는 것은 두 조건 다 만족할 때 True가 나오는 연산임


# In[28]:


#2차원 배열은 행렬로 행과 열로 구성됨


# In[30]:


c=np.array([[0,1,2],[3,4,5]]) #(2*3)의 배열이 반환됨.


# In[31]:


len(c) #두 개의 리스트로 구성되어 있음을 의미


# In[32]:


len(c[0]) #열의 개수


# In[33]:


#3차원 배열은 행과 열, 깊이로 구성됨


# In[34]:


d=np.array([[[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12]],
             [[11,12,13,14],
             [15,16,17,18],
             [19,20,21,22]]])


# In[35]:


d


# In[36]:


len(d) #행


# In[37]:


len(d[0]) #열


# In[38]:


len(d[0][0]) #깊이


# In[39]:


#배열 - 크기와 차원


# In[40]:


abc=np.array([1,2,3])


# In[41]:


print(abc.ndim)
print(abc.shape)


# In[42]:


b=np.array([[0,1,2],[3,4,5]])


# In[43]:


print(b.ndim)
print(b.shape)


# In[44]:


#1차원 배열의 인덱싱


# In[45]:


a=np.array([1,2,3,4])


# In[46]:


a[2]


# In[47]:


a[-1]


# In[48]:


#다차원 배열의 인덱싱


# In[49]:


b=np.array([[0,1,2],[3,4,5]])


# In[50]:


b


# In[53]:


b[0,0]


# In[52]:


b[1][2]


# In[54]:


#배열의 불리안 인덱싱


# In[59]:


a=np.array([0,1,2,3,4,5,6,7,8,9])

idx=np.array([True, False, True, False, True,
             False, True, False, True, False])

a[idx]


# In[60]:


a%2


# In[61]:


a%2==0


# In[62]:


a[a%2==0]


# In[63]:


#배열의 슬라이싱


# In[64]:


a=np.array([[0,1,2,3],[3,4,5,6,7]])
a


# In[68]:


a[0][:]


# In[70]:


a[:][1]


# In[72]:


a[:2][:2]


# In[73]:


#inf, non


# In[74]:


np.array([0,1,-1,0])/np.array([1,0,0,0])


# In[75]:


np.log(0)


# In[76]:


np.exp(-np.inf)


# In[77]:


#np.zeros


# In[79]:


a=np.zeros(5)
a


# In[81]:


b=np.zeros((2,3))
b


# In[82]:


c=np.zeros((5,2), dtype="i")
c


# In[83]:


#np.ones : 1로 초기화된 배열을 생성


# In[85]:


e=np.ones((2,3,4),dtype="i8")
e


# In[86]:


#np.arange : 특정한 규칙에 따라 증가하는 수열을 생성


# In[89]:


np.arange(10)


# In[90]:


np.arange(3,21,2)


# In[91]:


#전치 연산 : 행과 열을 바꾸는 전치 연산으로 t 속성 사용


# In[92]:


a=np.array([[1,2,3], [4,5,6]])
a


# In[93]:


a.T #3*2 행렬을 2*3으로 전치


# In[94]:


#배열의 크기 변환 : 원래 데이터는 보존한 상태로 형태만 reshape로 변형


# In[95]:


a=np.arange(12)
a


# In[96]:


b=a.reshape(3,4) #1차원 배열을 3*4 행렬로 변형
b


# In[97]:


#벡터화 연산 (두 벡터 연산)


# In[98]:


x=np.arange(1,10001)
y=np.arange(10001,20001)
x,y


# In[99]:


z=x+y
z


# In[100]:


#스칼라와 벡터 연산


# In[101]:


x=np.arange(10)
x


# In[102]:


100*x


# In[103]:


x=np.arange(12).reshape(3,4)
x


# In[104]:


100*x


# In[105]:


#배열의 브로드캐스팅 : 서로 다른 크기를 가진 두 배열의 사칙 연산에서 크기가 작은 배열을 자동으로 반복 확장하여 크기가 큰 배열에 맞춰준다.


# In[107]:


x=np.arange(5)
x


# In[108]:


x+1


# In[109]:


y=np.arange(3)
y


# In[110]:


x+y


# In[111]:


#차원 축소 연산


# In[112]:


y=np.array([1,2,3,1])
y


# In[113]:


y.mean() #평균


# In[114]:


np.median(y) #중간값


# In[118]:


x=np.array([[1,1],[2,2]])
x


# In[119]:


x.sum()


# In[120]:


x.sum(axis=0) #열 방향으로 계산


# In[121]:


x.sum(axis=1) #행 방향으로 계산


# In[ ]:




