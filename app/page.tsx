import Platform from './platform';import {getChatGPTUser} from './chatgpt-auth';
export const dynamic='force-dynamic';
export default async function Page(){const user=await getChatGPTUser();return <Platform initialNow={Date.now()} signedIn={!!user} initialName={user?.fullName?.split(' ')[0]??''}/>;}
