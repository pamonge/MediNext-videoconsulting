import React from 'react'
import { loginComponentStyles } from '../../styles/loginComponentStyles'

export const LoginComponent = () => {
  return (
    <div className={loginComponentStyles.container}>
        <div className={loginComponentStyles.modal}>
            <h3 className={loginComponentStyles.title}>
                Inicio de Sesión
            </h3>
            <form className={loginComponentStyles.form} action="">
                <div>
                    <label 
                    htmlFor="user"
                    className={loginComponentStyles.label}
                    >Ingrese usuario:</label>

                    <input 
                    type="text" 
                    name="user" 
                    id="user"
                    placeholder='ingrese su usuario' 
                    className={loginComponentStyles.input}/>
                </div>

                <div>
                    <label 
                    htmlFor="password"
                    className={loginComponentStyles.label}
                    >Ingrese contraseña:</label>

                    <input 
                    type="password" 
                    placeholder='**********'
                    className={loginComponentStyles.input}/>
                </div>

                <div className={loginComponentStyles.checkContainer}>
                    <div className='flex items-center'>
                        <input 
                        type="checkbox" 
                        name="remember" 
                        id="remember" 
                        className={loginComponentStyles.check}/>
                        <label htmlFor="remember" className={loginComponentStyles.checkLabel}>
                            Recordar sesión
                        </label>
                    </div>
                    <div className='text-sm'>
                        <a href="#" className={loginComponentStyles.recovery}>
                            Recuperar contraseña.
                        </a> 
                    </div>
                </div>
                <button type="submit" className={loginComponentStyles.button}>
                    Ingresar
                </button>
            </form>

        </div>

    </div>
  )
}
