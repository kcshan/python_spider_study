from lxml import etree
# nodename
# //
# /
# @ book[@id]

# /bookstore/book[1]
# /bookstore/book[last()]
# /bookstore/book[position()<3]
# /bookstore/book[last()]
# /book[@id="g_header"]

# *
# @*

# /book[@id="g_header"] | /bookstore/book[1]
# /book[@id="g_header" and @class="test"]
# /book[@id="g_header" or @class="test"]
# +
# -
# >=
# <=
# =
# /div[contains(@class, 'job_detail test')]
# 谓语中的下标是从1开始的

text = """
<table>
			    	<!-- 一个tr输入两个数据 -->
	    				    					    						    				<tr>
	    					    					<td>
	    						<a href="position_detail.php?id=45299" title="18402-MMO手游版本管理（深圳）">【深圳】18402-MMO手游...</a>
	    					</td>
	    					<td width="87" class="date">
	    						
	    					</td>
	    				    					    					<td>
	    						<a href="position_detail.php?id=45300" title="18402-移动游戏商业化运营（深圳）">【深圳】18402-移动游戏商...</a>
	    					</td>
	    					<td width="84" align="right" class="date">
	    						
	    					</td>
	    				    					    						    				</tr>
	    						    				<tr>
	    					    					<td>
	    						<a href="position_detail.php?id=45290" title="CS-战略传播经理">【深圳】CS-战略传播经理</a>
	    					</td>
	    					<td width="87" class="date">
	    						
	    					</td>
	    				    					    					<td>
	    						<a href="position_detail.php?id=45291" title="CS-产品运营经理">【深圳】CS-产品运营经理</a>
	    					</td>
	    					<td width="84" align="right" class="date">
	    						
	    					</td>
	    				    					    						    				</tr>
	    						    				<tr>
	    					    					<td>
	    						<a href="position_detail.php?id=45292" title="CS-项目经理">【深圳】CS-项目经理</a>
	    					</td>
	    					<td width="87" class="date">
	    						
	    					</td>
	    				    					    					<td>
	    						<a href="position_detail.php?id=45293" title="CS-项目总监">【深圳】CS-项目总监</a>
	    					</td>
	    					<td width="84" align="right" class="date">
	    						
	    					</td>
	    				    					    						    				</tr>
	    						    				<tr>
	    					    					<td>
	    						<a href="position_detail.php?id=45285" title="25663-腾讯云广电行业总监（北京/深圳）">【深圳】25663-腾讯云广电...</a>
	    					</td>
	    					<td width="87" class="date">
	    						
	    					</td>
	    				    					    					<td>
	    						<a href="position_detail.php?id=45265" title="25925-Linux C++开发工程师（深圳）">【深圳】25925-Linux C+...</a>
	    					</td>
	    					<td width="84" align="right" class="date">
	    						
	    					</td>
	    				    					    						    				</tr>
	    						    				<tr>
	    					    					<td>
	    						<a href="position_detail.php?id=45270" title="24012-H5游戏开发工程师（深圳）">【深圳】24012-H5游戏开发...</a>
	    					</td>
	    					<td width="87" class="date">
	    						
	    					</td>
	    				    					    					<td>
	    						<a href="position_detail.php?id=45264" title="27564-体育游戏社区运营（深圳）">【深圳】27564-体育游戏社...</a>
	    					</td>
	    					<td width="84" align="right" class="date">
	    						
	    					</td>
	    				    				    				</tr>
	    				    			</table>
"""


def parse_text():
    htmlElement = etree.HTML(text)
    print(type(htmlElement))
    print(etree.tostring(htmlElement, encoding="utf-8").decode("utf-8"))


def parse_tencent_file():
    htmlElement = etree.parse("tencent.html")
    # print(type(htmlElement))
    print(etree.tostring(htmlElement, encoding="utf-8").decode("utf-8"))


def parse_lagou_file():
    parser = etree.HTMLParser(encoding="utf-8")
    htmlElement = etree.parse("lagou.html", parser=parser)
    # print(type(htmlElement))
    print(etree.tostring(htmlElement, encoding="utf-8").decode("utf-8"))


if __name__ == "__main__":
    # parse_text()
    parse_tencent_file()
    # parse_lagou_file()