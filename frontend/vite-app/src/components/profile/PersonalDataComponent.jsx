import React, { useState } from 'react'
import defaultUser from '../../assets/defaultUser.png'
import { personalDataComponentStyles } from '../../styles/personalDataComponentStyles'

export const PersonalDataComponent = ({ userImg = defaultUser }) => {
    const [ formData, setFormData ] = useState({
        'name' : 'Juan',
        'lastName' : 'Perez',
        'dni' : '23456789',
        'date' : '01/01/00'
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
            
                <div className={personalDataComponentStyles.formColumn}>
                    <div className={personalDataComponentStyles.row}>
                        <label className={personalDataComponentStyles.label} htmlFor="name">Nombre</label>
                        <span className={personalDataComponentStyles.span} name='name' id='name' >{formData.name}</span>
                    </div>
                    <div className={personalDataComponentStyles.row}>
                        <label className={personalDataComponentStyles.label} htmlFor="lastName">Apellido</label>
                        <span className={personalDataComponentStyles.span} name='lastName'id='lastName'>{formData.lastName}</span>
                    </div>
                    <div className={personalDataComponentStyles.row}>
                        <label className={personalDataComponentStyles.label} htmlFor="dni">DNI</label>
                        <span className={personalDataComponentStyles.span} name="dni" id="dni">{formData.dni}</span>
                    </div>
                    <div className={personalDataComponentStyles.row}>
                        <label className={personalDataComponentStyles.label} htmlFor="dateBirth">Fecha de nacimiento</label>
                        <span className={personalDataComponentStyles.span} name="dateBirth" id="dateBirth">{formData.date}</span>
                    </div>
                </div>
            </div>
        </div>
    )
}
