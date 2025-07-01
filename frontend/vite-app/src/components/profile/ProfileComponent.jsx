import React from 'react'
import { NavBarComponent } from '../general/NavBarComponent'
import { PersonalDataComponent } from './PersonalDataComponent';
import { AffiliateComponent } from './AffiliateComponent';
import { profileComponentStyles } from '../../styles/profileComponentStyles';

export const ProfileComponent = () => {
  return (
    <div className={profileComponentStyles.profileContainer}>
        <NavBarComponent />
        <h2 className={profileComponentStyles.title}>
          	Perfil del Usuario
        </h2>
        <div className={profileComponentStyles.container} >
            <div className={profileComponentStyles.components}>
              	<PersonalDataComponent />
				<AffiliateComponent />
            </div>
        </div>
    </div>
  )
}

