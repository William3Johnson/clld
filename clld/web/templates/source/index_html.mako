<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>


<h2>${_('Sources')}</h2>
<p>
    ${_('Sources cited in this project')}
</p>
<div>
    ${ctx.render()}
</div>
