window.studioList = [{% for i in studioList %}"{{ i|escapejs }}"{% if not forloop.last %},{% endif %}{% endfor %}]
window.clientList = [{% for i in clientList %}"{{ i|escapejs }}"{% if not forloop.last %},{% endif %}{% endfor %}]
