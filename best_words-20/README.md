# Only the best words!

<sick rapper name> is feeling down about his latest record. Critics said that
"while <sick rapper name>'s beats are slammin', his word diversity is quite
lacking often leaving much to be desired." <sick rapper name> was devastated
at the news.

<sick rapper name> has never taken criticism that well, but you've
never seen him so low before. His apartment is a mess with him moping around
and spending most the day eating cereal and watching cable news. You decide
it's time for a rapid change. Maybe you could help him out by writing a word
analyzer?

You need something that can read in an album and find the best word in each
song (track):

> - The word cannot be used in any other track in the album.
> - The word needs to be used more than any other word on that track.
> - If two words in a track have the same usage count, note that:
>   - A longer word is better than a short word
>   - A higher lexicographical (`'z' > 'a'`) value is better than a low one

Think you can help get <sick rapper name> back on his game?

------------------------

## Input format

1. The first line, `n`, is an integer of the number of tracks in the album
2. The next line, `m`, is an integer of the number of words in a track.
3. The next line, `w`, is a string of a word in the track.
4. Goto 3 until there are no more words in that song.
5. Goto 2 until there are no more tracks.

###Constraints

- 2 <= n <= 20
- 2 <= m <= 700
- w is a lowercase string that only contains [a-z,\']

###Sample Input

    3
    7
    do
    you
    see
    what
    i
    can
    see
    7
    don't
    you
    think
    you
    can
    do
    better
    8
    zebrafish
    are
    better
    than
    clownfish
    don't
    you
    think

###Sample Output

    Track 0's best word is see
    Track 1 has no unique words
    Track 2's best word is zebrafish

--------------------------------------
## Running test cases

`best_words.py` is written in python3. If you want to run a test case you
can pipe the test case to the executable like so:

    cat testCase0.txt | python3 best_words.py
