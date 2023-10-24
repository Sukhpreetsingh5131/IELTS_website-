const APP_ID = 'a2fe2a6811784e5cbcd345267cc6df02';
const TOKEN = '007eJxTYHiWFczdWPLL717G4ujS0OiUB2+f7eILUK8JCfeY58dr06vAkGiUlmqUaGZhaGhuYZJqmpyUnGJsYmpkZp6cbJaSZmAUY7EipSGQkUGr8BozIwMEgvgcDOGJGanppUWlDAwAnmEgFQ==';

let client = null;
let localTracks = [];
let remoteUsers = {};

async function joinAndDisplayLocalStream(channelName) {
  try {
    client = AgoraRTC.createClient({ mode: 'rtc', codec: 'vp8' });

    await client.join(APP_ID, channelName, TOKEN, null);
    console.log("Joined channel successfully.");

    const localTrack = await AgoraRTC.createMicrophoneAudioTrack();
    localTracks.push(localTrack);

    await client.publish(localTracks);

    localTrack.play('local-stream');

    client.on('user-published', async (user, mediaType) => {
      await client.subscribe(user, mediaType);

      if (mediaType === 'audio') {
        const remoteAudioTrack = user.audioTrack;
        remoteUsers[user.uid] = remoteAudioTrack;

        const div = document.createElement('div');
        div.id = `remote-stream-${user.uid}`;
        document.getElementById('remote-streams-container').appendChild(div);

        remoteAudioTrack.play(`remote-stream-${user.uid}`);
      }
    });

    client.on('user-unpublished', (user) => {
      if (user.uid in remoteUsers) {
        remoteUsers[user.uid].stop();
        delete remoteUsers[user.uid];

        const div = document.getElementById(`remote-stream-${user.uid}`);
        div.parentNode.removeChild(div);
      }
    });
  } catch (error) {
    console.error('Failed to join the channel:', error);
  }
}

async function leaveChannel() {
  try {
    await client.leave();

    localTracks.forEach((track) => {
      track.stop();
      track.close();
    });
    localTracks = [];

    document.getElementById('local-stream').innerHTML = '';
    document.getElementById('remote-streams-container').innerHTML = '';

    console.log("Left channel successfully.");
  } catch (error) {
    console.error('Failed to leave the channel:', error);
  }
}

document.getElementById('create-button').addEventListener('click', async () => {
  const channelInput = document.getElementById('channel-input');
  const channelName = channelInput.value;
  await joinAndDisplayLocalStream(channelName);
});

document.getElementById('leave-button').addEventListener('click', leaveChannel);
