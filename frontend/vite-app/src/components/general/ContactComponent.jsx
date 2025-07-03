import React from 'react'
import { homeComponentStyles } from '../../styles/homeComponentStyles'
import emailImg from '../../assets/icons/email.png'
import marquerImg from '../../assets/icons/marker.png'
import phoneImg from '../../assets/icons/phone.png'
import wwwImg from '../../assets/icons/www.png'
// Consume los estilos de homeComponentStyles.js

export const ContactComponent = () => {
  return (
    <div>
        <p>
            Tenga persente nuestros medios de comunicación.
        </p>
        <ul className={homeComponentStyles.uList}>
            <li className={homeComponentStyles.listItem}>
                <img className={homeComponentStyles.image} src={emailImg} alt="email" />
                Email: <a className={homeComponentStyles.urlLink} href="mailto:medinextsalud@gmail.com">medinextsalud@gmail.com</a>.
            </li>
            <li className={homeComponentStyles.listItem}>
                <img className={homeComponentStyles.image} src={phoneImg} alt="phone" />
                Telefono: <a className={homeComponentStyles.urlLink} href="tel:02617459901">0261-7459901</a>.
            </li>
            <li className={homeComponentStyles.listItem}>
                <img className={homeComponentStyles.image} src={wwwImg} alt="website" />
                Envienos un correo o por Whatsapp desde nuestro sitio <a className={homeComponentStyles.urlLink} href="https://www.medinextsalud.com" target='_blank' >MediNext Salud</a>.
            </li>
            <li className={homeComponentStyles.listItem}>
                <img className={homeComponentStyles.image} src={marquerImg} alt="marker" />
                o visite nuestras oficinas en: <a className={homeComponentStyles.urlLink} href="https://maps.app.goo.gl/8oDs61mKNDh8Vqbd7" target='_blank'>Av. Colon 136, oficina 10, Mendoza, CP: M5502</a>.
            </li>
        </ul>
    </div>
  )
}
