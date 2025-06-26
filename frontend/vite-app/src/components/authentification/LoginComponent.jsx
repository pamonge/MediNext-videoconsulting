import React from 'react'

export const LoginComponent = () => {
  return (
    <div className='min-h-screen bg-gray-50 flex flex-col items-center justify-center p-4'>
        <div className='w-full max-w-md bg-white p-8 rounded-lg shadow-md'>
            <h3 className='text-2x1 font-bold text-center text-gray-800 mb-6'>
                Inicio de Seción
            </h3>
            <form className='space-y-6' action="">
                <div>
                    <label 
                    htmlFor="user"
                    className='block text-sm font-medium text-gray-700 mb-1'
                    >Ingrese usuario:</label>

                    <input 
                    type="text" 
                    name="user" 
                    id="user"
                    placeholder='ingrese su usuario' 
                    className='w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500'/>
                </div>

                <div>
                    <label 
                    htmlFor="password"
                    className='block text-sm font-medium text-gray-700 mb-1'
                    >Ingrese contraseña:</label>

                    <input 
                    type="password" 
                    placeholder='**********'
                    className='w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 font-medium'/>
                </div>

                <div className='flex items-center justify-between'>
                    <div className='flex items-center'>
                        <input 
                        type="checkbox" 
                        name="remember" 
                        id="remember" 
                        className='h-4 w-4 text-blue-600 focus:rising-blue-500 border-gray-300 rounded'/>
                        <label htmlFor="remember" className='ml-2 block text-sm text-gray-900'>
                            Recordar sesión
                        </label>
                    </div>
                    <div className='text-sm'>
                        <a href="#" className='font-medium text-blue-600 hover:text-blue-500'>
                            recuperar su contraseña.
                        </a> 
                    </div>
                </div>
                <button type="submit" className='w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-500 hover:bg-blue-400 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500'>
                    Ingresar
                </button>
            </form>

        </div>

    </div>
  )
}
