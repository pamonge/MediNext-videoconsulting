import React from 'react'
import { JitsiMeetingComponent } from './JitsiMeetingComponent'
import { NavBarComponent } from '../general/NavBarComponent'
import { videoCallComponentStyles } from '../../styles/videoCallComponentStyles'
import { EspecListComponent } from '../general/EspecListComponent'

export const VideoCallComponent = () => {
  return (
    <div>
        <NavBarComponent />
        <h2 className={videoCallComponentStyles.title}>Video Consulta</h2>
        <p>Seleccione de la especialidad solicitada</p>
        <EspecListComponent />
        <div className={videoCallComponentStyles.videoComponent}>
          <JitsiMeetingComponent  roomName='medico-afiliado' userName='Dr. Alguien' />
        </div>
    </div>
  )
}
