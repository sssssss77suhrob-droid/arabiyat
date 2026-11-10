import {bootstrap,json} from '../../../lib/server';
export const dynamic='force-dynamic';
export async function GET(){try{return json(await bootstrap());}catch(error){console.error('Bootstrap failed',error);return json({error:'Ma’lumotlarni yuklab bo‘lmadi. Qayta urinib ko‘ring.'},503);}}
