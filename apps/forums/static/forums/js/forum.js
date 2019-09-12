$(document).ready(function(){
    api_key = 1;
    $("p:nth-child(odd)").css("background-color", "#a8cdfe");

    $("p:nth-child(even)").css("background-color", "#eaeaea");


    $.get('https://www.thesportsdb.com/api/v1/json/' + api_key + '/lookupevent.php?id=' + EventId, function(res){
        NameofEvent = res.events[0].strEvent.toString();
        console.log(NameofEvent)
        $('.gamename').append(NameofEvent);

        if(res.events[0].intHomeScore != null){
            completed = "Game Completed";
            HomeTeam = res.events[0].strHomeTeam.toString();
            AwayTeam = res.events[0].strAwayTeam.toString();
            HomeScore = res.events[0].intHomeScore.toString();
            AwayScore = res.events[0].intAwayScore.toString();
            $('.gamedesc').append(completed + ': ' + HomeTeam + ' ' + HomeScore + ' | ' + AwayTeam + ' ' + AwayScore)


            $('.post_comment').hide();

            $('.gameover').append("Archived. Unable to post.")
        }
    }, "json");

    


});