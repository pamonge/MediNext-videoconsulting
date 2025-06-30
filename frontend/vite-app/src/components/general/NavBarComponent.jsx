import React from 'react'
import { NavLink } from 'react-router-dom'

export const NavBarComponent = () => {
	return (
		<div>
			<nav>
				<NavLink to='/home' >Inicio</NavLink>
				<NavLink to='/profile' >Perfil</NavLink>
				<NavLink to='/videocall'>Video Consulta</NavLink>
			</nav>
		</div>
	)
}
