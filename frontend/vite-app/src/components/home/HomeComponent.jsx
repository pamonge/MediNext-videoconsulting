import React from 'react'
import { NavLink } from 'react-router-dom'
import { NavBarComponent } from '../general/NavBarComponent';

export const HomeComponent = ({ nombre }) => {
	return (
		<div>
		<NavBarComponent />
		<div className='flex flex-col p-4 items-center'>
			<h1 className='text-center font-bold text-blue-600 text-4xl mt-4 mb-10'>MediNext Salud</h1>
			<h2 className='text-center text-xl m-4' >Bienvenido {nombre || 'Juan'} a la aplicación de autogestion de MediNext Salud</h2>
			<div className='flex flex-col w-md text-gray-700'>
				<p >
					Por intermedio de nuestra aplicación usted podrá:
					<ul className='flex flex-col gap-1 ml-6 list-image-[url(/src/assets/icons/blue-check.png)] list-inside'>
						<li className=''>Gestionar sus planes,</li>
						<li>Realizar video consultas medicas</li>
						<li>Gestionar beneficiarios</li>
						<li>Ver sus ultimos pagos realizados</li>
						<li>Consultar el estado de su cobertura</li>
						<li>Editar su perfil personal</li>
						<li>Solicitar atención personalizada con nuestros asesores</li>
						<li>Ver el estado de sus autorizaciones</li>
					</ul>
				</p>
				<p>
					Tenga persente nuestros medios de comunicación
					<ul>
						<li>Email: medinextsalud@gmail.com,</li>
						<li>Telefono: 0261-7459901,</li>
						<li>Envienos un correo o por Whatsapp desde nuestro sitio <a href="https://www.medinextsalud.com">MediNext Salud</a></li>
						<li>o visite nuestras oficinas en: <a href="https://maps.app.goo.gl/8oDs61mKNDh8Vqbd7">Av. Colon 136, oficina 10, Mendoza, CP: M5502</a></li>
					</ul>
				</p>
			</div>
			
		</div>
		</div>
	)
};
