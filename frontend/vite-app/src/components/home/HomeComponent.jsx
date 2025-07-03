import React, { useEffect, useState } from 'react'
import { NavBarComponent } from '../general/NavBarComponent';
import { homeComponentStyles } from '../../styles/homeComponentStyles';
import check from '../../assets/icons/blue-check.png'
import { appServicesData } from '../../data/appServicesData';
import { ContactComponent } from '../general/ContactComponent';

export const HomeComponent = ({ nombre }) => {
	const [ serviceData, setServiceData ] = useState([]);
	useEffect(() => {
		setServiceData(appServicesData)
	}, []);
	return (
		<div>
			<NavBarComponent />
			<div className={homeComponentStyles.containerNavBar}>
				<h1 className={homeComponentStyles.title}>MediNext Salud</h1>
				<h2 className={homeComponentStyles.welcomeMsj} >Bienvenido {nombre || 'Juan'} a la aplicación de autogestion de MediNext Salud</h2>
				<div className={homeComponentStyles.textContainer}>
					<p >
						Por intermedio de nuestra aplicación usted podrá:
					</p>
					<ul className={homeComponentStyles.uList}>
						{/* Informacion obtenida desde src/data/appServicesData */}
						{serviceData.map(
							(data, index) => (
								<li key={index} className={homeComponentStyles.listItem}> 
									<img className={homeComponentStyles.image} src={check} alt="check icon" />
									{data}
								</li>
							)
						)}		
					</ul>
					<ContactComponent />
				</div>
			</div>
		</div>
	)
};
