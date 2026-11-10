import type {Metadata} from 'next';
import './globals.css';
export const metadata:Metadata={title:'Arabiyat — Arab tili, sizning sur’atingizda',description:'Kitobni o‘qing, tinglang, so‘zlarni o‘rganing. Arab tilini o‘zbekcha yordam va shaxsiy o‘qish daftari bilan o‘rganish platformasi.',icons:{icon:'/favicon.svg'},manifest:'/manifest.webmanifest',appleWebApp:{capable:true,title:'Arabiyat',statusBarStyle:'black-translucent'}};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="uz" dir="ltr"><body>{children}</body></html>;}
