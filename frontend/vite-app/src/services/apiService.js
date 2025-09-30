import axios from 'axios'

const API_BASE_URL = 'http://127.0.0.1:8000/api/';  // <<< Reemplazar en produccion

// Obtener CSRF token de las cookies
const getCSRFToken = () => {
  const name = 'csrftoken';
  let cookieValue = null;
  
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Añadir CSRF token automáticamente a todas las requests
api.interceptors.request.use(
  (config) => {
    // Solo añadir CSRF para métodos que lo requieren
    if (['post', 'put', 'patch', 'delete'].includes(config.method)) {
      config.headers['X-CSRFToken'] = getCSRFToken();
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Crear instancia de axios con configuracion basica
const djangoApi = axios.create({
    baseURL: API_BASE_URL,
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json',
    },
})

export const apiService = {
  // USUARIOS  --------------------------------------------
  // Obtener todos los usuarios  
  getAllUsers : () => djangoApi.get('users/'),

  // Obtener un usuario por id
  getUser : (id) => djangoApi.get(`users/${id}`),

  // PLANES  ----------------------------------------------
  // Otener todos los planes
  getAllPlans : () => djangoApi.get('medical-plans/'),

  // Obtener un plan según id
  getPlan : (id) => djangoApi.get (`medical_plans/${id}`),

  // PAGOS  -----------------------------------------------
  // Obtener todos los pagos
  getAllPayments : () => djangoApi.get('payments/'),

  // Obtener un pago según id
  getPayment : (id) => djangoApi.get(`payments/${id}`),

  // PERFIL  ---------------------------------------------
  // Obtener un perfil por id
  getProfile : (id) => djangoApi.get(`profiles/${id}`),

  // Historias Medicas ----------------------------------
  // Obtener una historia medica por id
  getMedicalHistory : (id) => djangoApi.get(`medical-histories/${id}`),

  // ARCHIVOS PARA AUTORIZAR  ---------------------------
  // Obtener todos los archivos para autorizar
  getAllAuthorizationFiles : () => djangoApi.get('upload-files/'),

  // Otener un archivo para autorizar por id
  getAuthorizationFile : (id) => djangoApi.get(`upload-files/${id}`),
}  