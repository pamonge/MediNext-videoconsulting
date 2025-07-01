import React, { useState } from 'react'
import { affiliateComponentStyles } from '../../styles/affiliateComponentStyles';

export const AffiliateComponent = () => {
  const [ planStatus, setPlanStatus ] = useState(true);
  const [ formData, setFormData ] = useState({
    socNumber : '1111111',
    beneficiary : 'somebody',
    dischargeDate : '01/01/2025',
    plan : 'Basic',
  });

  const handleClick = () => {
    setPlanStatus(!planStatus);
  } 

  return (
    <div className={affiliateComponentStyles.container}>
        <h3 className={affiliateComponentStyles.title}>
            Datos del afiliado
        </h3>
        <div className={affiliateComponentStyles.formColumn}>
            <div className={affiliateComponentStyles.row}>
                <label className={affiliateComponentStyles.label} htmlFor="socNumber">Numero de afiliado</label>
                <span className={affiliateComponentStyles.span} name="socNumber" id="socNumber">{formData.socNumber}</span>
            </div>
            <div className={affiliateComponentStyles.row}>
                <label className={affiliateComponentStyles.label} htmlFor="beneficiary">Beneficiario</label>
                <span className={affiliateComponentStyles.span} name='beneficiary' id='beneficiary'>{formData.beneficiary}</span>
            </div>
            <div className={affiliateComponentStyles.row}>
                <label className={affiliateComponentStyles.label} htmlFor="dischargeDate">Fecha de alta</label>
                <span className={affiliateComponentStyles.span} name='dischargeDate' id='dischargeDate'>{formData.dischargeDate}</span>
            </div>
            <div className={affiliateComponentStyles.row}>
                <label className={affiliateComponentStyles.label} htmlFor="plan">Plan contratado</label>
                <span className={affiliateComponentStyles.span} name='plan' id='plan'>{formData.plan}</span>
            </div>
            <div className={affiliateComponentStyles.row}>
                <label className={affiliateComponentStyles.label} htmlFor="estado">Cobertura</label>
                <span className={`${affiliateComponentStyles.span} ${ planStatus===true ? affiliateComponentStyles.enable : affiliateComponentStyles.disable }`}  name="estado" id='estado'>{planStatus==true ? 'Vigente' : 'Sin Cobertura'}</span>
            </div>
            <button onClick={handleClick}>Click</button>
        </div>
        
    </div>
  )
}
