###!
 * Baruwa Enterprise Edition
 * http://www.baruwa.com
 *
 * Copyright (c) 2013-2015 Andrew Colin Kissa
 *
 *
###
$ = jQuery
exports = this
exports.setitems_url = setitems_url
style_map = {gray: 'notscanned', whitelisted: 'whitelisted', blacklisted: 'blacklisted', highspam: 'highspam', spam: 'spam', infected: 'infected', white: ''}

show_dialog = () ->
    bootbox.dialog '<h3 class="head smaller lighter blue">Processing your request, please be patient</h3>',
    [{'label': 'Dismiss', 'class': 'btn btn-small btn-success'}]

disable_links = (e) ->
    if exports.inprogress
        e.preventDefault()
        e.stopPropagation()
        # bootbox.dialog '<h3 class="head smaller lighter blue">Processing your request, please be patient</h3>',
        # [{'label': 'Dismiss', 'class': 'btn btn-small btn-success'}]
    1

pagination = (data) ->
    if data.items.length
        rows = []
        if data.next_page != data.first_page and data.page != data.first_page
            if data.section
                rows.push '<span><a href="/messages/quarantine/{{section}}/{{order_by}}/{{direction}}/{{first_page}}"><i class="icon-double-angle-left"></i></a></span><span>...</span>'
            else
                rows.push '<span><a href="/messages/quarantine/{{order_by}}/{{direction}}/{{first_page}}"><i class="icon-double-angle-left"></i></a></span><span>...</span>'
        if data.previous_page
            if data.section
                rows.push '<span><a href="/messages/quarantine/{{section}}/{{order_by}}/{{direction}}/{{previous_page}}"><i class="icon-angle-left"></i></a></span>'
            else
                rows.push '<span><a href="/messages/quarantine/{{order_by}}/{{direction}}/{{previous_page}}"><i class="icon-angle-left"></i></a></span>'
        for linkpage in data.page_nums
            if linkpage == data.page
                rows.push '<span class="curpage">{{page}}</span>'
            else
                if data.section
                    rows.push '<span><a href="/messages/quarantine/{{section}}/{{order_by}}/{{direction}}/'+linkpage+'">'+linkpage+'</a></span>'
                else
                    rows.push '<span><a href="/messages/quarantine/{{order_by}}/{{direction}}/'+linkpage+'">'+linkpage+'</a></span>'
        if data.next_page
            if data.section
                rows.push '<span><a href="/messages/quarantine/{{section}}/{{order_by}}/{{direction}}/{{next_page}}"><i class="icon-angle-right"></i></a></span>'
            else
                rows.push '<span><a href="/messages/quarantine/{{order_by}}/{{direction}}/{{next_page}}"><i class="icon-angle-right"></i></a></span>'
        if data.next_page != data.page_count and data.page != data.page_count and data.page_count != 0
            if data.section
                rows.push '<span>...</span><span><a href="/messages/quarantine/{{section}}/{{order_by}}/{{direction}}/{{last_page}}"><i class="icon-double-angle-right"></i></a></span>'
            else
                rows.push '<span>...</span><span><a href="/messages/quarantine/{{order_by}}/{{direction}}/{{last_page}}"><i class="icon-double-angle-right"></i></a></span>'
        tmpl = rows.join '\n'
        html = $.mustache tmpl, data
    else
        html = '-'
    html

ajaxify = (e, url) ->
    if exports.inprogress
        show_dialog
        return false
    e.preventDefault()
    $.address.value url.replace(/\.json/, '')
    $.address.history $.address.baseURL() + url
    ajaxrequest url
    1

replacelink = (html, style)->
    $(style).html html
    1

buildrows = (items) ->
    row = '<tr class="{{style}}"><td class="select_row">' +
            '<input type="checkbox" name="message_id" value="{{id}}" class="selector" /></td>' +
            '<td class="date_td hidden-phone"><a href="/messages/detail/{{id}}">{{timestamp}}</a></td>' +
            '<td class="from_row hidden-phone"><a href="/messages/detail/{{id}}">{{from_address}}</a></td>' +
            '<td class="to_row hidden-phone"><a href="/messages/detail/{{id}}">{{to_address}}</a></td>' +
            '<td class="subject_row"><a href="/messages/detail/{{id}}">{{subject}}</a></td>' +
            '<td class="score_row hidden-phone"><a href="/messages/detail/{{id}}">{{sascore}}</a></td>' +
            '<td class="status_row hidden-phone"><a href="/messages/detail/{{id}}">{{status}}</a></td></tr>'
    if items.length
        rows = []
        $.each items, (i,n) ->
            n['timestamp'] = BaruwaDateString(n['timestamp'])
            n['style'] = style_map[n['style']]
            html = $.mustache row, n
            rows.push html
        replacement = rows.join ''
    else
        replacement = '<tr><td colspan="7" class="spanrow">'+gettext('No messages found')+'</td></tr>'
    $('tbody').empty().append replacement
    1

buildpage = (data) ->
    buildrows data.items
    $('div.pages').html pagination(data)
    if data.items.length
        pages_tmpl = gettext('Showing items {{first_item}} to {{last_item}} of {{item_count}}.')
        pages_html = $.mustache pages_tmpl, data
        title_tmpl = gettext('Messages :: Quarantine :: Showing page {{page}} of {{page_count}} pages.')
        title_html = $.mustache title_tmpl, data
        $('div.limiter').show()
    else
        pages_html = gettext('No items found')
        title_html = gettext('Messages :: Quarantine')
        $('div.limiter').hide()
    $('div.toolbar p').html pages_html
    $('#title').html title_html
    $.address.title '.:. ' + exports.baruwa_custom_name + ' :: ' + title_html
    $('div.pages a').click((e)->
        url = $(this).attr('href') + '.json'
        ajaxify(e, url)
    )
    columns = ['timestamp', 'from_address', 'to_address', 'subject', 'sascore']
    linfo = [gettext('Date/Time'), gettext('From'), gettext('To'), gettext('Subject'), gettext('Score')]
    style = ['.qdate_heading', '.from_heading', '.to_heading', '.subject_heading', '.score_heading']
    tmpl = '<a href="/messages/quarantine/{{order_by}}/{{direction}}/1">{{column}}</a>'
    for column, i in columns
        html = $.mustache tmpl, {'order_by': column, 'direction': data.direction, 'column': linfo[i]}
        if column == data.order_by
            if data.direction == 'dsc'
                newdirection = 'asc'
                c = '&nbsp;&uarr;'
            else
                newdirection = 'dsc'
                c = '&nbsp;&darr;'
            arrow = $.mustache tmpl, {'order_by': data.order_by, 'direction': newdirection, 'column': c}
            html = html + arrow
        replacelink html, style[i]
        1
    $('thead a').click((e)->
        url = $(this).attr('href') + '.json'
        ajaxify(e, url)
    )
    if $('#alertmsg').length
        $('#alertmsg').empty()
        $('#alertmsg').remove()

ajaxrequest = (url) ->
    if not $('#shield').length
        $('#wrap').after exports.loading
    else
        $('#shield').show()
    $.ajax url,
        type:'GET',
        cache:false,
        dataType:'json',
        beforeSend: (XHR)->
            exports.inprogress = true
            1
        error: display_ajax_error,
        success:buildpage,
        complete:(XHR, textStatus) ->
            exports.inprogress = false
            $('#shield').hide()
            if $(window).scrollTop()
                $('html,body').animate
                    scrollTop: $("#wrap").offset().top, 1500
            1
    1

$(document).ready ->
    $('#allchecker').click(->
        $('.selector').attr 'checked', this.checked
        1
    )
    exports.inprogress = false
    $('div.pages a').click((e)->
        url = $(this).attr('href') + '.json'
        ajaxify(e, url)
    )
    $('thead a').click((e)->
        url = $(this).attr('href') + '.json'
        ajaxify(e, url)
    )
    $('a').click disable_links
    $.address.externalChange((e)->
        if e.path == '/'
            $.address.history $.address.baseURL()
            return
        url = $.address.value() + '.json'
        ajaxify(e, url)
        1
    )
    $('#squarantinetop, #squarantinebottom').change(->
        n = $(this).val()
        location.href = "#{exports.setitems_url}?n=#{n}"
    )
    $('.filter_add').unbind 'click'
    $('.filter_add').bind 'click', (e)->
        e.preventDefault()
        e.stopPropagation()
        if exports.inprogress
            show_dialog()
            return false
        add_filters()
        1
    $('.filter_show').unbind 'click'
    $('.filter_show').bind 'click', (e)->
        e.preventDefault()
        e.stopPropagation()
        if exports.inprogress
            show_dialog()
            return false
        show_filters()
        1
    1


