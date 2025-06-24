import React from 'react';
import { JitsiMeeting } from '@jitsi/react-sdk';

export const JitsiMeetingComponent = ({ roomName = 'TestRoom', userName = 'Invitado' }) => {
  return (
    <div>
      <h2>Videollamada en curso</h2>
      <JitsiMeeting
        domain="meet.jit.si"
        roomName={roomName}
        configOverwrite={{
          startWithAudioMuted: true,
          disableModeratorIndicator: true,
          startScreenSharing: true,
          enableEmailInStats: false
        }}
        interfaceConfigOverwrite={{
          DISABLE_JOIN_LEAVE_NOTIFICATIONS: true
        }}
        userInfo={{
          displayName: userName
        }}
        getIFrameRef={(iframeRef) => {
          iframeRef.style.height = "500px";
          iframeRef.style.width = "100%";
        }}
      />
    </div>
  )
}
