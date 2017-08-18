# urls_list format :
# [{link},{fonction/file_url},{0 for fonction,1 for file_url}]

import web.home.views as home

urls_list = [
	['/',home.home, 0],
	['/labitedemarinestdeg','home/index.html', 1],
	['/brous','brous.html',['x','y'], 1],
	
]