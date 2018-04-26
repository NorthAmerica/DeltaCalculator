from time import time
from math import exp, sqrt, log
from random import gauss, seed

class MonteCarlo():
	def __init__(self,s_0):
		self.S_0 = s_0  # 股票或指数初始的价格;
		self.K = 105  # 行权价格
		self.T = 1.0  # 期权的到期年限(距离到期日时间间隔)
		self.r = 0.05  # 无风险利率
		self.sigma = 0.2  # 波动率(收益标准差)
		self.M = 50  # number of time steps
		self.dt = self.T / self.M  # time enterval
		self.I = 20000  # number of simulation

	def gaussNum(self):
		X = []
		for i in range(self.I):
			Y = []
			for t in range(self.M + 1):
				Y.append(gauss(0.0, 1.0))
			X.append(Y)
		return X

	def calculate(self,gaussNumList):
		#return "test"00001 = {list} <class 'list'>: [99.99, 102.86011630742232, 104.24165020390205, 102.65685948266858, 101.78084967756426, 104.96137455151245, 106.05720286666298, 104.27979725116205, 104.79870074597518, 103.89881927788097, 100.6887749243186, 103.9102664272708, 99.83103977570481, 100.86519704833022, 98.56482199590772, 97.88829873431068, 93.45467821681251, 97.09292510373982, 104.34014589298305, 100.67647549394378, 107.68924298848431, 109.04074631018283, 107.49314901530991, 106.56799242058044, 106.08350787913587, 110.0380726998316, 109.7582648937012, 109.70869390586603, 108.68052442954071, 113.24314668369334, 112.32393931634937, 110.70765126816266, 116.40143488194144, 120.84356470461049, 120.29681017549304, 131.13193938070674, 133.5349298930271, 131.52513681796464, 134.40648774465868, 135.68463951441896, 131.54136015943772, 129.3030761016875, 126.96865396919505, 128.8897554615372, 129.63869703157044, 136.1856837240021, 135.01744384144996, 136.36770093956315, 136.197359150209, 135.0133348796828, 132.28987116...… View
		#seed(2000)
		#start = time()
		S = []  #
		for i in range(self.I):
			path = []  # 时间间隔上的模拟路径
			for t in range(self.M + 1):
				if t == 0:
					path.append(self.S_0)
				else:
					# k = gauss(0.0,1.0)
					z = gaussNumList[i][t]
					S_t = path[t - 1] * exp((self.r - 0.5 * self.sigma ** 2) * self.dt + self.sigma * sqrt(self.dt) * z)
					path.append(S_t)
			S.append(path)
		# 计算期权现值
		C_0 = exp(-self.r * self.T) * sum([max(path[-1] - self.K, 0) for path in S]) / self.I
		#total_time = time() - start
		return C_0
		# print
		# 'European Option value %.6f' % C_0
		# print
		# 'total time is %.6f seconds' % total_time