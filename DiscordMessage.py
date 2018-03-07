#self.id
#self.channel_id
#self.author
#self.content
#self.timestamp
#self.edited_timestamp
#
#SOME OTHER STUFF



#ideas

#is command
#sent by object?

from DiscordUser import DiscordUser

class DiscordMessage:


	def __init__(self,messageArray):
		self.content = messageArray['content']
		#create user object
		self.author = DiscordUser(messageArray['author'])

	def isValidCommand():
		if message.startswith('!'):
			return True