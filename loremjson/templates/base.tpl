<html>
    <head>
        <meta http-equiv="Content-type" content="text/html; charset=utf-8"/>
        <title>{% block title %}{{ title }}{% endblock %} - Lorem JSON</title>
        <link rel="stylesheet" href="/static/css/bootstrap.css">
        <link rel="stylesheet" href="/static/css/main.css" type="text/css" media="screen" charset="utf-8">
        {% block header %}
          
        {% endblock %}
    </head>
    <body>
        <div id="content">
        {% block content %}
            Content here
        {% endblock %}
        </div>
    </body>
</html>