import sys
import textwrap
from sports_naarad.extern.tabulate import tabulate


def main():
    """\
    Usage: sports-naarad [-h] [-F] [-C] live_score|news|[player_stats name] [-my_fav_team]

    Get latest updates for football and cricket

    Options:

    -h, --help                shows help(this) message

    -F, --football [uefa,
    barclay, fifa]            Get football updates. The tournament for which you
                              want to get updates. One of the argumets from uefa,
                              barclay and fifa is compulsory.

    -C, --cricket             Get cricket updates for international matches.

    [live-score, news,
    ,fixtures
    player-stats[name]]       Fields to get. `live-scores` to get live socre of
                              on-going matches, `news` to get latest news headlines,
                              `player-stats` to get statistics of player specified.
                              `fixtures` to get updates on upcoming matches.
                              Compulsory single argument. For football option you
                              can give additional options topscorer.
                              Use `-` instead of space in names.

    --proxy                   To specify proxy. Defaults to system proxy. Take name of
                              a file. Sample -proxy http://username:password@host:port/
    
    --unset-proxy             Removes the proxy set by using --proxy option.
    """
    useage = textwrap.dedent(main.__doc__)
    args = sys.argv
    if args[1] == '-h':
        print(useage)
        sys.exit(0)
    try:
        if '--proxy' in args:
            with open(sys.path[0] + '/proxy.config', 'w') as f:
                f.write(args[args.index('-proxy') + 1])
        if '--unset-proxy' in args:
            import os
            os.reomve(sys.path[0] + '/proxy.config')
        if args[1] == '-F' or args[1] == '--football' or args[1] == '-f':
            if '-c' in args or '-C' in args or '--cricket' in args:
                raise ValueError(
                    'Both Football and cricket cannot be specified')
            if args[2] == 'uefa':
                pass
            elif args[2].lower() == 'barclay':
                from sports_naarad.barclay import Barclay
                if args[3].lower() == 'fixtures':
                    fixture = Barclay().Fixtures(type_return='dict')
                    header = ['Clubs', 'Time(UTC)', 'Location']
                    print(tabulate(fixture, headers=header,
                                   tablefmt='fancy_grid', floatfmt=".2f"))
                elif args[3].lower() == 'live-score':
                    print('\n'.join(Barclay().liveScore(type_return='dict')))
                elif args[3].lower() == 'news':
                    news = Barclay().get_news_headlines(type_return='dict')
                    print()
                    for headline in news:
                        print('Headline: ' + headline + '\n' +
                              'link: ' + news[headline] + '\n')
                elif args[3].lower() == 'player-stats':
                    stats = Barclay().playerStats(args[4], type_return='dict')
                    print()
                    for stat in stats:
                        print(stat + ': ' + stats[stat])
                elif args[3].lower() == 'topscorer':
                    scorers = Barclay().topScorers(type_return='dict')
                    top_scorers = []
                    for names in scorers:
                        top_scorers.append((names, scorers[names]))
                    top_scorers = sorted(top_scorers, key=lambda x: int(x[1]))
                    top_scorers.reverse()
                    print(tabulate(top_scorers, headers=[
                          'Player Name', 'Goal Scored'], tablefmt='fancy_grid'))
                else:
                    raise ValueError(
                        'Not a Valid argument!\n Use -h option for help.')
            elif args[2] == 'fifa':
                pass
            else:
                raise ValueError(
                    'Not a Valid argument!\n Use -h option for help')
        if args[1] == '-C' or args[1] == '-c' or args[1] == '--cricket':
            from sports_naarad.cricketAPI import Cricket
            if '-f' in args or '--football' in args:
                raise ValueError(
                    'Both Cricket and Football cannot be specifed together!')
            if args[2].lower() == 'live-score':
                print(Cricket().live_score(type_return='dict'))
            elif args[2].lower() == 'fixtures':
                tournaments = Cricket().list_matches(type_return='dict')
                header = ['Teams', 'Time and Date', 'Venue', 'Result']
                for tournament in tournaments:
                    print("Tournament: {}".format(tournament))
                    print(
                        tabulate(tournaments[tournament], headers=header, tablefmt='fancy_grid'))
                    print('\n')
            elif args[2].lower() == 'news':
                news = Cricket().news(type_return='dict')
                print()
                for headline in news:
                    print('Headline: ' + headline + '\n' +
                          'link: ' + news[headline] + '\n')
            elif args[2].lower() == 'player-stats':
                try:
                    stats = Cricket().get_player_stats(
                        args[3], type_return='dict')
                    print('\n')
                    for stat in stats:
                        print(stat + ': ' + stats[stat])
                except:
                    raise ValueError('Not a Valid Name!')
            else:
                raise ValueError(
                    'Not a Valid Argument! Use -h or --help for help ')
    except IndexError:
        print("Arguments not according to format. Please see help! Use -h option for help")


if __name__ == '__main__':
    main()
