// app.js
const APP_ID = 'e704d8257c444002aa7103740725bb0d';
const CHANNEL = 'guru';
const TOKEN = '007eJxTYMj7Vej9t/rAmYfefgrHKlcpTFl4rGDPi+lP4gSLHHcLzchTYEg1NzBJsTAyNU82MTExMDBKTDQ3NDA2NzEwNzJNSjJIWeRxPqUhkJHhAMMDBkYoBPFZGNJLi0oZGADEyiCg';
let UID


const client=AgoraRTC.createClient({mode:'rtc',codec:'h264'})
let localTracks=[]
let remoteUsers={}
let joinAndDisplayLocalStream=async()=> {
   UID= await client.join(APP_ID,CHANNEL,TOKEN,null)
   localTracks=AgoraRTC.createMicrophone()
   let_player=
   
}