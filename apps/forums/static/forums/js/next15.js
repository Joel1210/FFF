$(document).ready(function () {
    api_key = 1;
    NFL_Id = 4391;

    $.get('https://www.thesportsdb.com/api/v1/json/' + api_key + '/eventsnextleague.php?id=' + NFL_Id, function (res) {
        NameofLeague = res.events[0].strLeague.toString();
        console.log(NameofLeague)
        $('.LeagueName').append(NameofLeague);

        for (var i = 0; i < 15; i++) {
            var html_str = "";
            eventid = res.events[i].idEvent.toString();
            html_str += "<tr><td><h3><a href='/forums/" + eventid + "'><b>" + res.events[i].strEvent + "</b></a></h3></td></tr>";
            html_str += "<tr><td>" + res.events[i].dateEvent + "</td></tr>";
            html_str += "<tr><td>" + res.events[i].strTime + "</td></tr>";
            $('.Gametitle').append(html_str)
        };
    }, "json");

});