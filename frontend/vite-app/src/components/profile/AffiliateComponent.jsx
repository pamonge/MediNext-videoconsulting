import React, { useState } from 'react'

export const AffiliateComponent = () => {
  const [ planStatus, setPlanStatus ] = useState('Vigente');

  return (
    <div>
        <h3>Datos del afiliado</h3>
        <div>
            <label htmlFor="socNumber">Numero de afiliado</label>
            <input type="number" name="socNumber" id="socNumber" />
        </div>
        <div>
            <label htmlFor="beneficiary">Beneficiario</label>
            <input type="text" name='beneficiary' id='beneficiary' />
        </div>
        <div>
            <label htmlFor="dischargeDate">Fecha de alta</label>
            <input type="date" name='dischargeDate' id='dischargeDate' />
        </div>
        <div>
            <label htmlFor="plan">Plan contratado</label>
            <input type="text" name='plan' id='plan' />
        </div>
        <div>
            <label htmlFor="estado">Estado</label>
            <span name="estado" id='estado'>{planStatus}</span>
        </div>
    </div>
  )
}
