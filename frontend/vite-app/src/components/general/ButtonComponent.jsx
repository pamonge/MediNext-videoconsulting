import React from 'react'
import { buttonComponentStyles } from '../../styles/buttonComponentStyles'

export const ButtonComponent = ( { func, value } ) => {
  return (
    <button onClick={func} className={buttonComponentStyles.genButton} >{value}</button>
  )
}
