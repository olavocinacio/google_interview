# Lidando com inputs em python:
# input1 = raw_input("Digite algo aqui também: "); # Assume que o input é uma string
input2 = input("Digite algo aqui também: "); #  it assumes the input is a valid Python expression and returns the evaluated result to you. (You can insert python code and the operations would be done)

# Abrindo um arquivo:
# file object = open(file_name [, access_mode][, buffering]); 
# f = open("test.txt", mode='r', encoding='utf-8'); # with all the specifications
# f = open("test.txt")    # open file in current directory
# f = open("C:/Python38/README.txt")  # specifying full path
# with open(<file name>, <access mode>) as <file-pointer>:
# 	#Statement suite  #-> Abrindo usando with. Ao sair da identação, o arquivo é fechado automaticamente

# Criando um arquivo:
# arquivo = open("teste.txt", "a");

# Percorrendo um arquivo:
# for i in fileptr:    
# 	print(i) # i contains each line of the file     

# Access modes:
'''
r -> Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.

rb -> Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.

r+ -> Opens a file for both reading and writing. The file pointer placed at the beginning of the file.

rb+ -> Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.

w -> pens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

wb -> Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

w+ -> Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

wb+ -> Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

a -> pens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

ab -> Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

a+ -> Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
	
ab+ -> Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing

x	-> Opens a file for exclusive creation. If the file already exists, the operation fails.

t	-> Opens in text mode. (default)

+	-> Opens a file for updating (reading and writing) -> example: f = open("img.bmp",'r+b')# read and write in binary mode

'''

# buffering − If the buffering value is set to 0, no buffering takes place. If the buffering value is 1, line buffering is performed while accessing a file. If you specify the buffering value as an integer greater than 1, then buffering action is performed with the indicated buffer size. If negative, the buffer size is the system default(default behavior).

# File object attributes:
# file.closed -> Returns true if file is closed, false otherwise.
# file.mode -> Returns access mode with which file was opened.
# file.name -> Returns name of the file.
# file.softspace -> Returns false if space explicitly required with print, true otherwise.

# Fechando um arquivo:
# fileObject.close(); -> close() method flushes any unwirtten infromation and closes the file object, after which no more writing can be done. 

# Escrevendo em um arquivo:
# fileObject.write(string); -> Adiciona um \n e em seguida a string ao arquivo

# lendo um arquivo:
#fileObject.read([count]); -> Here, passed parameter is the number of bytes to be read from the opened file. This method starts reading from the beginning of the file and if count is missing, then it tries to read as much as possible, maybe until the end of file.

# Posição de arquivos:
#The tell() method tells you the current position within the file; in other words, the next read or write will occur at that many bytes from the beginning of the file.
# The seek(offset[, from]) method changes the current file position. The offset argument indicates the number of bytes to be moved. The from argument specifies the reference position from where the bytes are to be moved.
# If from is set to 0, it means use the beginning of the file as the reference position and 1 means use the current position as the reference position and if it is set to 2 then the end of the file would be taken as the reference position.

# Renomeando um arquivo:
# import os;
# os.rename(current_file_name, new_file_name);

# Deletando arquivos:
# import os;
# os.remove(file_name);

# Criando um novo diretório(pasta):
# import os;
# os.mkdir("newdir");

# Mudando o diretório atual:
# import os;
# os.chdir("newdir")

# Mostrando o diretório atual;
# import os;
# os.getcwd();

# Deletar um diretório:
# import os;
# os.rmdir("dirname");


# Mais alguns métodos e propriedades: ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# detach()	-> Separates the underlying binary buffer from the TextIOBase and returns it.
# isatty()	-> Returns True if the file stream is interactive.
# readable() -> Returns True if the file stream can be read from.
# seekable() -> Returns True if the file stream supports random access.
# writable() -> Returns True if the file stream can be written to.
# 1	file.close() -> Close the file. A closed file cannot be read or written any more.
# 2	file.flush() -> Flush the internal buffer, like stdio's fflush. This may be a no-op on some file-like objects.
# 3	file.fileno() -> Returns the integer file descriptor that is used by the underlying implementation to request I/O operations from the operating system.
# 4	file.isatty() -> Returns True if the file is connected to a tty(-like) device, else False.
# 5	file.next() -> Returns the next line from the file each time it is being called.
# 6	file.read([size]) -> Reads at most size bytes from the file (less if the read hits EOF before obtaining size bytes).
# 7	file.readline([size]) -> Reads one entire line from the file. A trailing newline character is kept in the string.
# 8	file.readlines([sizehint]) -> Reads until EOF using readline() and return a list containing the lines. If the optional sizehint argument is present, instead of reading up to EOF, whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read.
# 9	file.seek(offset[, whence]) -> Sets the file's current position
# 10	file.tell() -> Returns the file's current position
# 11	file.truncate([size]) -> Truncates the file's size. If the optional size argument is present, the file is truncated to (at most) that size.
# 12	file.write(str) -> Writes a string to the file. There is no return value.
# 13	file.writelines(sequence) -> Writes a sequence of strings to the file. The sequence can be any iterable object producing strings, typically a list of strings.
# 1	os.access(path, mode) -> Use the real uid/gid to test for access to path.
# 2	os.chdir(path) -> Change the current working directory to path
# 3	os.chflags(path, flags) -> Set the flags of path to the numeric flags.
# 4	os.chmod(path, mode) -> Change the mode of path to the numeric mode.
# 5	os.chown(path, uid, gid) -> Change the owner and group id of path to the numeric uid and gid.
# 6	os.chroot(path) -> Change the root directory of the current process to path.
# 7	os.close(fd) -> Close file descriptor fd.
# 8	os.closerange(fd_low, fd_high) -> Close all file descriptors from fd_low (inclusive) to fd_high (exclusive), ignoring errors.
# 9	os.dup(fd) -> Return a duplicate of file descriptor fd.
# 10	os.dup2(fd, fd2) -> Duplicate file descriptor fd to fd2, closing the latter first if necessary.
# 11	os.fchdir(fd) -> Change the current working directory to the directory represented by the file descriptor fd.
# 12	os.fchmod(fd, mode) -> Change the mode of the file given by fd to the numeric mode.
# 13	os.fchown(fd, uid, gid) -> Change the owner and group id of the file given by fd to the numeric uid and gid.
# 14	os.fdatasync(fd) -> Force write of file with filedescriptor fd to disk.
# 15	os.fdopen(fd[, mode[, bufsize]]) -> Return an open file object connected to the file descriptor fd.
# 16	os.fpathconf(fd, name) -> Return system configuration information relevant to an open file. name specifies the configuration value to retrieve.
# 17	os.fstat(fd) -> Return status for file descriptor fd, like stat().
# 18	os.fstatvfs(fd) -> Return information about the filesystem containing the file associated with file descriptor fd, like statvfs().
# 19	os.fsync(fd) -> Force write of file with filedescriptor fd to disk.
# 20	os.ftruncate(fd, length) -> Truncate the file corresponding to file descriptor fd, so that it is at most length bytes in size.
# 21	os.getcwd() -> Return a string representing the current working directory.
# 22	os.getcwdu() -> Return a Unicode object representing the current working directory.
# 23	os.isatty(fd) -> Return True if the file descriptor fd is open and connected to a tty(-like) device, else False.
# 24	os.lchflags(path, flags) -> Set the flags of path to the numeric flags, like chflags(), but do not follow symbolic links.
# 25	os.lchmod(path, mode) -> Change the mode of path to the numeric mode.
# 26	os.lchown(path, uid, gid) -> Change the owner and group id of path to the numeric uid and gid. This function will not follow symbolic links.
# 27	os.link(src, dst) -> Create a hard link pointing to src named dst.
# 28	os.listdir(path) -> Return a list containing the names of the entries in the directory given by path.
# 29	os.lseek(fd, pos, how) -> Set the current position of file descriptor fd to position pos, modified by how.
# 30	os.lstat(path) -> Like stat(), but do not follow symbolic links.
# 31	os.major(device) -> Extract the device major number from a raw device number.
# 32	os.makedev(major, minor) -> Compose a raw device number from the major and minor device numbers.
# 33	os.makedirs(path[, mode]) -> Recursive directory creation function.
# 34	os.minor(device) -> Extract the device minor number from a raw device number.
# 35	os.mkdir(path[, mode]) -> Create a directory named path with numeric mode mode.
# 36	os.mkfifo(path[, mode]) -> Create a FIFO (a named pipe) named path with numeric mode mode. The default mode is 0666 (octal).
# 37	os.mknod(filename[, mode=0600, device]) -> Create a filesystem node (file, device special file or named pipe) named filename.
# 38	os.open(file, flags[, mode]) -> Open the file file and set various flags according to flags and possibly its mode according to mode.
# 39	os.openpty() -> Open a new pseudo-terminal pair. Return a pair of file descriptors (master, slave) for the pty and the tty, respectively.
# 40	os.pathconf(path, name) -> Return system configuration information relevant to a named file.
# 41	os.pipe() -> Create a pipe. Return a pair of file descriptors (r, w) usable for reading and writing, respectively.
# 42	os.popen(command[, mode[, bufsize]]) -> Open a pipe to or from command.
# 43	os.read(fd, n) -> Read at most n bytes from file descriptor fd. Return a string containing the bytes read. If the end of the file referred to by fd has been reached, an empty string is returned.
# 44	os.readlink(path) -> Return a string representing the path to which the symbolic link points.
# 45	os.remove(path) -> Remove the file path.
# 46	os.removedirs(path) -> Remove directories recursively.
# 47	os.rename(src, dst) -> Rename the file or directory src to dst.
# 48	os.renames(old, new) -> Recursive directory or file renaming function.
# 49	os.rmdir(path) -> Remove the directory path
# 50	os.stat(path) -> Perform a stat system call on the given path.
# 51	os.stat_float_times([newvalue]) -> Determine whether stat_result represents time stamps as float objects.
# 52	os.statvfs(path) -> Perform a statvfs system call on the given path.
# 53	os.symlink(src, dst) -> Create a symbolic link pointing to src named dst.
# 54	os.tcgetpgrp(fd) -> Return the process group associated with the terminal given by fd (an open file descriptor as returned by open()).
# 55	os.tcsetpgrp(fd, pg) -> Set the process group associated with the terminal given by fd (an open file descriptor as returned by open()) to pg.
# 56	os.tempnam([dir[, prefix]]) -> Return a unique path name that is reasonable for creating a temporary file.
# 57	os.tmpfile() -> Return a new file object opened in update mode (w+b).
# 58	os.tmpnam() -> Return a unique path name that is reasonable for creating a temporary file.
# 59	os.ttyname(fd) -> Return a string which specifies the terminal device associated with file descriptor fd. If fd is not associated with a terminal device, an exception is raised.
# 60	os.unlink(path) -> Remove the file path.
# 61	os.utime(path, times) -> Set the access and modified times of the file specified by path.
# 62	os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]]) -> Generate the file names in a directory tree by walking the tree either top-down or bottom-up.
# 63	os.write(fd, str) -> Write the string str to file descriptor fd. Return the number of bytes actually written.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------