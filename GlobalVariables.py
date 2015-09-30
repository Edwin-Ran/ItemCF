#coding=utf-8

#ininiation data based on user and song
DictBasedOnUser = dict();
DictBasedOnSong = dict();

#matrix ,column and row both are songid,and the numbers in matrix means how many user both like i , j,so the diagonal are 0 or none
MatrixForSong = dict();

#how many user or how manu times are the song download
SongDownloadNum = dict();

#matrix fro Similarity that describe the Similarity of two different songs
MatrixForSimilarity = dict();
