#-*- coding:utf-8 –*-
import re
s = "1.躯干肌张力减退;震颤;僵硬;视神经萎缩;听力障碍;共济失调;讲话与语言发展延迟;小脑萎缩;矮小;智力残疾;视力障碍;特殊性学习障碍;脑髓鞘形成减少;脑白质营养不良;运动延迟;小头畸形;眼球震颤;说话少;癫痫发作;舞蹈手足徐动症;肌张力障碍;构音困难;四肢瘫痪;|2.四肢肌张力障碍;泛发性肌张力障碍;扭转性肌张力障碍;斜颈;构音障碍;吞咽困难;共济失调步态;|3.先天性肌纤维障碍病"
pattern = "(\d)(\.)([^\d]+)(\|)"
result = re.match(pattern,s)
match = re.compile(r"(\d)(\.)([^\d]+)(\|)")
re = match.findall(s)
print(re[1][2])