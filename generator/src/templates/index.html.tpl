<h1>References</h1>

<ul>
{% for filename, name in filenames.iteritems() %}
    <li>
        <a href="{{filename}}" title="Description of {{name}}">{{name}}</a>
    </li>
{% endfor %}
</ul>