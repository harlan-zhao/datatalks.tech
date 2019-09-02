# datatalks.tech
Check www.datatalks.tech for api usage and other information

API useage
Endpoint
www.datatalks.tech/getvisual

Methods
Only POST would be accepted

Body Format
{col1_title : 'your column_1 title',
col2_title : 'your column_2 title',
col1_data : 'your column_1 data here',
col2_data : 'your column_2 data here'}


Example of POST body format
{'col1_title' : 'month',
'col2_title' : 'day',
'col1_data' : '[Jan,Mar,Apr]',
'col2_data' : '[2,3,4]'}


Example Response
{ "div": "the diagram html code chunk, you can implement it directly in your webpage",
"js" : "The JavaScript code chunk, should be used along with the html code" }
