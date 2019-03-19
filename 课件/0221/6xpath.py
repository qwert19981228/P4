from  lxml import etree

text = '''
<div class="odiv">
    <div></div>
    <div item="666" ></div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a>
            <ul></ul>
         </li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
     </ul>
 </div>
 <div item="777">
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-01"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
     </ul>
 </div>
'''

html = etree.HTML(text)
# // 忽略之前的元素 从当前位置开始
# ./ 当前元素
# @属性名     获取属性的值
# res = html.xpath('//a/text()')
# res = html.xpath('//a/@href')
# res = html.xpath('//div/ul')
# res = html.xpath('//@class')
# res = html.xpath('//div/@item')
# 找第一个ul下第一个li的class属性的值
# res = html.xpath('//div[@class="odiv"]/ul/li[1]/@class')
# 获取最后一个li的class值
# res = html.xpath('//div[2]/ul/li[last()]/@class')
# 找到属性为item的div
res = html.xpath('//div[@*]')
res = html.xpath('/html/*')
res = html.xpath('/html/body/div | /html/body')   # 或者  取并集
print(res)

# for i in res:
#     res2 = i.xpath('./text()')
#     print(res2)
