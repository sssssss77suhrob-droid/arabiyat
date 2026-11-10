import {env} from 'cloudflare:workers';
import {eq,sql} from 'drizzle-orm';
import {getDb} from '../db';
import {aiUsage} from '../db/schema';
export class AIServiceError extends Error {constructor(message:string,public status=503,public code='unavailable'){super(message);}}
export async function takeAITurn(userId:string,limit=8){const minute=Math.floor(Date.now()/60000);const rows=await getDb().insert(aiUsage).values({userId,minute,count:1}).onConflictDoUpdate({target:[aiUsage.userId,aiUsage.minute],set:{count:sql`${aiUsage.count}+1`}}).returning();if(rows[0].count>limit)throw new AIServiceError('Bir oz kuting, keyin qayta urinib ko‘ring.',429,'rate_limit');}
export async function openAI(path:string,body:FormData|Record<string,unknown>){
 if(!env.OPENAI_API_KEY)throw new AIServiceError('Jonli izoh xizmati hali ulanmagan.',503,'not_configured');
 const form=body instanceof FormData;
 const response=await fetch('https://api.openai.com/v1/'+path,{method:'POST',headers:{Authorization:'Bearer '+env.OPENAI_API_KEY,...(form?{}:{'Content-Type':'application/json'})},body:form?body:JSON.stringify(body),signal:AbortSignal.timeout(55000)});
 const data=await response.json() as any;
 if(!response.ok){const code=data.error?.code??'provider_error';throw new AIServiceError(code==='credit_balance_exhausted'||code==='insufficient_quota'?'Jonli xizmat uchun API krediti qolmagan. Administrator hisobni to‘ldirishi kerak.':'Jonli xizmat hozir javob bermadi. Keyinroq urinib ko‘ring.',response.status===429?503:502,code);}
 return data;
}
export async function digest(value:string){return [...new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(value)))].map(x=>x.toString(16).padStart(2,'0')).join('');}
export function outputText(data:any){return data.output?.flatMap((o:any)=>o.content??[]).filter((c:any)=>c.type==='output_text').map((c:any)=>c.text??'').join('')??'';}
