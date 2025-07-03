import React from 'react'
import { NavLink } from 'react-router-dom'
import { navBarComponentStyles } from '../../styles/navBarComponentStyles'

export const NavBarComponent = () => {
	return (
		<div className={navBarComponentStyles.navBarContainer}>
			<nav className={navBarComponentStyles.navLabel}>
				<div className={navBarComponentStyles.navLinkList}>
					<NavLink className={navBarComponentStyles.navLink} to='/home' >Inicio</NavLink>
					<NavLink className={navBarComponentStyles.navLink} to='/profile' >Perfil</NavLink>
					<NavLink className={navBarComponentStyles.navLink} to='/video'>Video Consulta</NavLink>
				</div>
			</nav>
		</div>
	)
}
