import React from 'react';
import { ButtonComponent } from '../general/ButtonComponent';

export const JitsiMeetingComponent = ({ 
  roomName = 'TestRoom', 
  userName = 'Invitado',
  width = 800,
  height = 600
}) => {
  const openJitsiInNewWindow = () => {
    // Configuración para la nueva ventana
    const config = {
      roomName: roomName,
      width: '100%',
      height: '100%',
      configOverwrite: {
        startWithAudioMuted: true,
        disableModeratorIndicator: true,
        startScreenSharing: true,
        enableEmailInStats: false
      },
      interfaceConfigOverwrite: {
        DISABLE_JOIN_LEAVE_NOTIFICATIONS: true
      },
      userInfo: {
        displayName: userName
      }
    };

    // Construir URL con parámetros
    const params = new URLSearchParams();
    params.append('config', JSON.stringify(config.configOverwrite));
    params.append('interfaceConfig', JSON.stringify(config.interfaceConfigOverwrite));
    params.append('userInfo', JSON.stringify(config.userInfo));
    
    const jitsiUrl = `https://meet.jit.si/${config.roomName}?${params.toString()}`;
    
    // Abrir en nueva ventana
    window.open(
      jitsiUrl,
      '_blank',
      `width=${width},height=${height},menubar=no,toolbar=no,location=no,personalbar=no`
    );
  };

  return (
    <div>
      <h2>Preparado la video consulta</h2>
      <ButtonComponent func={openJitsiInNewWindow} value='Iniciar video consulta'/>
    </div>
  );
};