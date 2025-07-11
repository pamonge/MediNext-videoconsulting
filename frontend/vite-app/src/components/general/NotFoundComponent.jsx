import React from 'react'
import failImg from "../../assets/icons/fail.png"
import { ButtonComponent } from './ButtonComponent'
import { NavLink, useNavigate } from 'react-router-dom'
import { notFoundComponentStyles } from '../../styles/notFoundComponentStyles'

export const NotFoundComponent = () => {

	const navigate = useNavigate();

	const goBack = () => {
		navigate('/home')
	}

	return (
		<div className={notFoundComponentStyles.container}>
			<div>
				<img className={notFoundComponentStyles.img} src={failImg} alt="Fail image" />
			</div>
			<div className={notFoundComponentStyles.textContainer}>
				<h3 className={notFoundComponentStyles.title}>Pagina no encontrada</h3>
				<p className={notFoundComponentStyles.paragraph}>
					Por favor, comuniquese con 
					<NavLink className={notFoundComponentStyles.navlink} to={'/support'}>soporte</NavLink> 
					o regrese al inicio</p>
				<ButtonComponent func={goBack} value='Volver al inicio' />
			</div>
		</div>
	)
}
