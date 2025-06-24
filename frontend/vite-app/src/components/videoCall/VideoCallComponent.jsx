import React from 'react'
import { JitsiMeetingComponent } from './JitsiMeetingComponent'

export const VideoCallComponent = () => {
  return (
    <div>
        <h1>Video llamada</h1>
        <JitsiMeetingComponent roomName='medico-afiliado' userName='Dr. Alguien' />
    </div>
  )
}
