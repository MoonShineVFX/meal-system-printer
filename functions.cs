[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern int usbportwrite(byte[] VId, byte[] PId, uint iLen, byte[] Data);

[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern int comportwrite(byte[] Com,
                                    uint BaudRate,
                                    byte Parity,
                                    byte ByteSize,
                                    byte fDtrControl,
                                    byte StopBits,
                                    uint iLen,
                                    byte[] Data);

[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern int Netportwrite(uint addr, uint port, uint Timeout, uint iLen, byte[] Data);

[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern int Lptportwrite(byte[] Name, uint iLen, byte[] Data);

/*
*网络函数
*/
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern bool InitNetSev();
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern int ConnectNetPort(uint addr, uint port, uint Timeout);
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern int WriteToNetPort(UInt16 fs, byte[] SendBuf, UInt16 WriteSize);
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern int ReadFromNetPort(UInt16 fs, byte[] RecvBuf, UInt16 RecvBufSize);
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern bool CloseNetPor(UInt16 fs);
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern bool CloseNetServ();

/*
*USB接口
*/
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern int OpenUsb(byte[] vid, byte[] pid);
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern int WriteUsb(UInt16 fs, byte[] SendBuf, UInt16 SendBufSize);
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern int ReadUsb(UInt16 fs, byte[] ReadBuf, UInt16 ReadBufSize);
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern bool CloseUsb(UInt16 fs);

/*
*并口接口
*/
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern int OpenLptW(byte[] Name);
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern int WriteLpt(UInt16 fs, byte[] SendBuf, UInt16 SendBufSize);
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern int ReadLpt(UInt16 fs, byte[] ReadBuf, UInt16 ReadBufSize);
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern bool CloseLpt(UInt16 fs);
/*
*串口接口
*/
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern int OpenComW(byte[] Com, uint BaudRate, Byte Parity, Byte ByteSize, Byte fDtrControl, Byte StopBits);
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern int ReadCom(UInt16 fs, byte[] ReadBuf, UInt16 SendBufSize);
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern int WriteCom(UInt16 fs, byte[] SendBuf, UInt16 WriteSize);
[DllImport("JsPrinterDll.dll", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
public static extern bool CloseCom(UInt16 fs);