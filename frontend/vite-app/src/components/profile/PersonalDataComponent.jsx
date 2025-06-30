import React, { useState } from 'react'
import defaultUser from '../../assets/defaultUser.png'
import { personalDataComponentStyles } from '../../styles/personalDataComponentStyles'

export const PersonalDataComponent = ({ userImg = defaultUser }) => {
    const [ formData, setFormData ] = useState({
        'name' : '',
        'lastName' : '',
        'dni' : '',
        'date' : ''
    })
    return (
        <div className={personalDataComponentStyles.personalDataContainer} >
            <h3 className={personalDataComponentStyles.title}>
                Datos Personales
            </h3>
            <div className={personalDataComponentStyles.dataContainer} >
                <div className={personalDataComponentStyles.imgContainer}>
                    <img className={personalDataComponentStyles.img} src={ userImg } alt="user image" />
                </div>
            
                <div>
                    <div>
                        <label className={personalDataComponentStyles.label} htmlFor="name">Nombre</label>
                        <input className={personalDataComponentStyles.input} type="text" name='name' id='name' value={formData.name}/>
                    </div>
                    <div>
                        <label className={personalDataComponentStyles.label} htmlFor="lastName">Apellido</label>
                        <input className={personalDataComponentStyles.input} type="text" name='lastName'id='lastName' value={formData.lastName}/>
                    </div>
                    <div>
                        <label className={personalDataComponentStyles.label} htmlFor="dni">DNI</label>
                        <input className={personalDataComponentStyles.input} type="number" name="dni" id="dni" value={formData.dni}/>
                    </div>
                    <div>
                        <label className={personalDataComponentStyles.label} htmlFor="dateBirth">Fecha de nacimiento</label>
                        <input className={personalDataComponentStyles.input} type="text" name="dateBirth" id="dateBirth" value={formData.date}/>
                    </div>
                </div>
            </div>
        </div>
    )
}
